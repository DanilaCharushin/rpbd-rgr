import Vue from "vue";
import Vuex from "vuex";
import config from "../config";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    users: [],
    types: []
  },
  mutations: {
    commitUsers(state, users) {
      state.users = users;
    },
    commitTypes(state, types) {
      state.types = types;
    },
  },
  actions: {
    async fetchAll({commit}) {
      let url = `${config.host}/all`;
      console.log("fetching GET for url " + url);
      const users = await (await fetch(url)).json();
      console.log("users response:");
      console.log(users);
      commit("commitUsers", users);

      url = `${config.host}/types`;
      console.log("fetching GET for url " + url);
      const types = await (await fetch(url)).json();
      console.log("types response:");
      console.log(types);
      commit("commitTypes", types);

      return this;
    },

    async insertUser({commit}, user) {
      let url = `${config.host}/all`;
      console.log("fetching POST for url " + url);
      const users = await (await fetch(url, {
        method: "POST",
        body: JSON.stringify(user),
        headers: {
          "Content-Type": "application/json"
        }
      })).json();
      console.log("users response:");
      console.log(users);
      commit("commitUsers", users);

      return this;
    },

    async updateUser({commit}, user) {
      let url = `${config.host}/one/${user.id}`;
      console.log("fetching PUT for url " + url);
      const users = await (await fetch(url, {
        method: "PUT",
        body: JSON.stringify(user),
        headers: {
          "Content-Type": "application/json"
        }
      })).json();
      console.log("users response:");
      console.log(users);
      commit("commitUsers", users);

      return this;
    },

    async removeUser({commit}, user) {
      let url = `${config.host}/one/${user.id}`;
      console.log("fetching DELETE for url " + url);
      const users = await (await fetch(url, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json"
        }
      })).json();
      console.log("users response:");
      console.log(users);
      commit("commitUsers", users);

      return this;
    },
  },
  getters: {
    getUsers: state => {
      return state.users;
    }
  },
  modules: {}
});
