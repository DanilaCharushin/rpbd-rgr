<template>
  <div class="user">
    <div class="user-info">
      <span>{{ user.name }}</span>
      <span>{{ user.address }}</span>
      <div class="btn-group" role="group">
        <button :id="'phones' + user.id" aria-expanded="false" aria-haspopup="true"
                class="btn btn-secondary dropdown-toggle"
                data-toggle="dropdown" type="button">
          Phones
        </button>
        <div class="dropdown-menu">
          <a v-for="phone in this.user.phones" :key="phone.id" :href="'tel:' + phone.number" class="phone">
            <span>{{ phone.number }}</span>
            <span class="material-icons">{{ getPhoneTypeIcon(phone) }}</span>
          </a>
        </div>
      </div>
    </div>
    <div class="user-actions">
      <span :data-target="'#edit-modal' + user.id" class="btn btn-outline-primary" data-toggle="modal">Edit</span>
      <span class="btn btn-outline-danger" @click="remove()">Remove</span>
    </div>
    <div :id="'edit-modal' + user.id" aria-hidden="true" class="modal fade" role="dialog" tabindex="-1">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Edit user "{{ user.name }}"</h5>
          </div>
          <div class="modal-body">
            <form>
              <div class="form-group">
                <label :for="'name'+user.id">Name</label>
                <input :id="'name'+user.id" v-model="newName" :placeholder="newName" class="form-control"
                       type="text">
              </div>
              <div class="form-group">
                <label :for="'address'+user.id">Address</label>
                <input :id="'address'+user.id" v-model="newAddress" :placeholder="user.address" class="form-control"
                       type="text">
              </div>

              <div v-for="phone in this.newPhones" :key="phone.id" class="phone">
                <input :id="phone.id" v-model="phone.number" :placeholder="phone.number"
                       class="form-control"
                       type="tel">
                <div v-for="type in $store.state.types" :key="type.id"
                     class="form-check form-check-inline phone-type-radio">
                  <input
                    :id="'phone' + phone.id + 'phone-type' + type.id"
                    v-model="phone.type"
                    :name="'phone-type' + phone.id"
                    :value="type.name"
                    class="form-check-input"
                    type="radio"
                  >
                  <label :for="'phone' + phone.id + 'phone-type' + type.id"
                         class="form-check-label">{{ type.name }}</label>
                </div>
                <span class="btn btn-danger" @click="removePhone(phone)">X</span>
              </div>

              <div class="phone">
                <input
                  :id="'newPhoneNumber' + user.id"
                  v-model="newPhoneNumber"
                  class="form-control"
                  placeholder="add new phone"
                  type="tel">
                <div v-for="type in $store.state.types" :key="type.id"
                     class="form-check form-check-inline phone-type-radio">
                  <input
                    :id="'user' + user.id + 'new-phone-type' + type.id"
                    v-model="newPhoneType"
                    :name="'new-phone-type' + user.id"
                    :value="type.name"
                    class="form-check-input"
                    type="radio"
                  >
                  <label :for="'user' + user.id + 'new-phone-type' + type.id"
                         class="form-check-label">{{ type.name }}</label>
                </div>
              </div>

              <div class="modal-footer">
                <button class="btn btn-primary" type="button" @click="rollback()">Rollback</button>
                <button class="btn btn-secondary" data-dismiss="modal" type="button">Close</button>
                <button class="btn btn-success" data-dismiss="modal" type="button" @click="saveChanges()">Save changes
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "User",
  props: ["user"],
  data() {
    return {
      newName: this.user.name,
      newAddress: this.user.address,
      newPhones: this.user.phones,
      newPhoneNumber: "",
      newPhoneType: "mobile"
    }
  },
  methods: {
    ...mapActions(["updateUser", "removeUser"]),
    rollback() {
      this.newName = this.user.name;
      this.newAddress = this.user.address;
      this.newPhones = this.user.phones;
      this.newPhoneNumber = "";
      this.newPhoneType = "mobile";
    },
    remove() {
      this.removeUser(this.user);
    },
    getPhoneTypeIcon(phone) {
      return phone.type === "mobile" ? "phone_iphone" : phone.type;
    },
    async saveChanges() {
      if (!this.newName && !this.newAddress) {
        return;
      }
      console.log(this.user.phones);
      console.log(this.newPhones);

      if (this.newPhoneNumber) {
        this.newPhones.push({
          number: this.newPhoneNumber,
          type: this.newPhoneType
        });
        this.newPhoneNumber = "";
        this.newPhoneType = "mobile";
      }
      await this.updateUser({
        id: this.user.id,
        name: this.newName,
        address: this.newAddress,
        phones: this.newPhones
      });
    },
    removePhone(phone) {
      this.newPhones = this.newPhones.filter(p => p.id !== phone.id);
    }
  }
}
</script>

<style>
.user {
  display: flex;
  justify-content: space-between;
}

.user-info {
  flex-basis: 80%;
  display: flex;
  justify-content: space-between;
}

.dropdown-menu {
  width: 150px;
  left: -30px !important;
}

.phone {
  display: flex;
  justify-content: space-between;
  padding: 0.5em;
}

.phone-type-radio {
  margin: 0 0.5em;
}
</style>