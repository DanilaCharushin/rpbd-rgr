<template>
  <div class="container">
    <header class="header">
      <h1>
        {{ currentUsers.length === 0 ? "Phonebook is empty" : "Phonebook users count: " + currentUsers.length }}
      </h1>
      <button class="btn btn-success" data-target="#add-new-user-modal" data-toggle="modal">Add new user</button>
    </header>
    <div class="search">
      <div class="form-check">
        <input id="searchByFourDigits" v-model="searchByFourDigits" class="form-check-input" type="checkbox"
               value="true" @change="search()">
        <label class="form-check-label" for="searchByFourDigits">
          Search by the last 4 digits of the phone
        </label>
      </div>
      <div class="form-group">
        <input v-model="searchText" class="form-control" placeholder="type here for search users..." type="text"
               @input="search()">
      </div>
    </div>

    <hr>

    <div id="add-new-user-modal" aria-hidden="true" class="modal fade" role="dialog" tabindex="-1">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add new user</h5>
            <button aria-label="Close" class="close" data-dismiss="modal" type="button">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="form-group">
                <label for="name">Name</label>
                <input id="name" v-model="newName" class="form-control" placeholder="ex: Freddie Mercury"
                       type="text">
              </div>
              <div class="form-group">
                <label for="address">Address</label>
                <input id="address" v-model="newAddress" class="form-control"
                       placeholder="ex: u. Pushkina, d. Kolotushkina"
                       type="text">
              </div>

              <div class="form-group">
                <label for="newHomeNumber">Home phone number</label>
                <input id="newHomeNumber" v-model="newHomeNumber" class="form-control" type="tel">
              </div>
              <div class="form-group">
                <label for="newWorkNumber">Work phone number</label>
                <input id="newWorkNumber" v-model="newWorkNumber" class="form-control" type="tel">
              </div>
              <div class="form-group">
                <label for="newMobileNumber">Mobile phone number</label>
                <input id="newMobileNumber" v-model="newMobileNumber" class="form-control" type="tel">
              </div>

              <div class="modal-footer">
                <button class="btn btn-secondary" data-dismiss="modal" type="button">Close</button>
                <button class="btn btn-success" data-dismiss="modal" type="button" @click="addNewUser()">Save changes
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>


    <ul>
      <li
        v-for="user in currentUsers"
        :key="user.id"
      >
        {{ user.id }}
        <User :user="user"/>
      </li>
    </ul>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
import User from "./User";

export default {
  components: {
    User
  },
  data() {
    return {
      newName: "",
      newAddress: "",
      newHomeNumber: "",
      newWorkNumber: "",
      newMobileNumber: "",
      searchText: "",
      searchByFourDigits: false,
      currentUsers: [],
      allUsers: []
    };
  },
  async created() {
    await this.fetchAll();
    this.allUsers = this.$store.state.users;
    this.currentUsers = Array.from(this.allUsers);
  },
  computed: {
    ...mapGetters["getUsers"],
  },
  methods: {
    ...mapActions(["fetchAll", "insertUser"]),
    async addNewUser() {
      if (!this.newAddress && !this.newName) {
        return;
      }
      let phones = []
      if (this.newMobileNumber) {
        phones.push({
          number: this.newMobileNumber,
          type: "mobile"
        });
      }
      if (this.newWorkNumber) {
        phones.push({
          number: this.newWorkNumber,
          type: "work"
        });
      }
      if (this.newHomeNumber) {
        phones.push({
          number: this.newHomeNumber,
          type: "home"
        });
      }
      await this.insertUser({
        name: this.newName,
        address: this.newAddress,
        phones: phones,
      });

      this.currentUsers = this.allUsers = this.getUsers;
      this.newAddress = "";
      this.newName = "";
      this.newMobileNumber = "";
      this.newWorkNumber = "";
      this.newHomeNumber = "";
    },
    search() {
      if (!this.searchText) {
        this.currentUsers = this.allUsers;
      } else {
        this.currentUsers = this.allUsers.filter(user => {
          if (this.searchByFourDigits) {
            for (const phone of user.phones) {
              if (phone.number.slice(-4).includes(this.searchText)) {
                return true;
              }
            }
          } else {
            if (user.name.toLowerCase().includes(this.searchText.toLowerCase())
              || user.address.toLowerCase().includes(this.searchText.toLowerCase())) {
              return true;
            }
            for (const phone of user.phones) {
              if (phone.number.includes(this.searchText)) {
                return true;
              }
            }
          }
          return false;
        });
      }
    }
  }
};
</script>
<style>

/* CSS declarations go here */
body {
  padding: 10px;
  font-family: sans-serif;
  background-color: #315481;
  background-image: linear-gradient(to bottom, #315481, #918e82 100%);
  background-attachment: fixed;

  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;

  padding: 0;
  margin: 0;

  font-size: 14px;
}

.container {
  margin: 0 auto;
  min-height: 100%;
  background: white;
}

header {
  background: #d2edf4;
  background-image: linear-gradient(to bottom, #d0edf5, #e1e5f0 100%);
  padding: 20px 15px 15px 15px;
  position: relative;
}

#login-buttons {
  display: block;
}

h1 {
  font-size: 1.5em;
  margin: 0;
  margin-bottom: 10px;
  display: inline-block;
  margin-right: 1em;
}

form {
  margin-top: 10px;
  margin-bottom: -10px;
  position: relative;
}

.new-task input {
  box-sizing: border-box;
  padding: 10px 0;
  background: transparent;
  border: none;
  width: 100%;
  padding-right: 80px;
  font-size: 1em;
}

.new-task input:focus {
  outline: 0;
}

ul {
  margin: 0;
  padding: 0;
  background: white;
}

.delete {
  float: right;
  font-weight: bold;
  background: none;
  font-size: 1em;
  border: none;
  position: relative;
}

li {
  position: relative;
  list-style: none;
  padding: 15px;
  border-bottom: #eee solid 1px;
}

li .text {
  margin-left: 10px;
}

li.checked {
  color: #888;
}

li.checked .text {
  text-decoration: line-through;
}

li.private {
  background: #eee;
  border-color: #ddd;
}

header .hide-completed {
  float: right;
}

.toggle-private {
  margin-left: 5px;
}

@media (max-width: 600px) {
  li {
    padding: 12px 15px;
  }

  .search {
    width: 150px;
    clear: both;
  }

  .new-task input {
    padding-bottom: 5px;
  }
}

.header {
  display: flex;
  justify-content: space-between;
}

.search {
  margin: 2em 0;
}
</style>