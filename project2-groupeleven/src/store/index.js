import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);

const state = {//要设置的全局访问的state对象
    showLoading: false,
    changableNum: 0
    //要设置的初始属性值
};
const getters = {   //实时监听state值的变化(最新状态)
    isShow(state) {  //方法名随意,主要是来承载变化的showLoading的值
        return state.showLoading
    },
    getChangedNum() {  //方法名随意,主要是用来承载变化的changableNum的值
        return state.changebleNum
    }
};
const mutations = {
    show(state) {   //自定义改变state初始值的方法，这里面的参数除了state之外还可以再传额外的参数(变量或对象);
        state.showLoading = true;
    },
    hide(state) {  //同上
        state.showLoading = false;
    },
    newNum(state, sum) { //同上，这里面的参数除了state之外还传了需要增加的值sum
        state.changableNum += sum;
    }
};
const actions = {
    hideLoading(context) {  //自定义触发mutations里函数的方法，context与store 实例具有相同方法和属性
        context.commit('hide');
    },
    showLoading(context) {  //同上注释
        context.commit('show');
    },
    getNewNum(context, num) {   //同上注释，num为要变化的形参
        context.commit('newNum', num)
    }
};
const store = new Vuex.Store({
    state,
    getters,
    mutations,
    actions
});

export default store;