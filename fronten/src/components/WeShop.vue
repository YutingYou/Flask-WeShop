<template>
  <div>
    <van-row class="goods" gutter="20">
      <van-col span="8" v-for="goods in goodsList" key="goods.radio_name">
        <van-row>
          <img :src="goods.img_url" :alt="goods.radio_text" @click="reverseMessage(goods.radio_name)">
        </van-row>
        <van-row>
          <van-col span="8" offset="8">
            <van-radio :name="goods.radio_name" v-model="radioSelected">{{goods.radio_text}}</van-radio>
          </van-col>
        </van-row>
      </van-col>
    </van-row>
    <van-button type="primary" @click="chooseAddress">Primary</van-button>
  </div>
</template>

<script>
  import img1 from '../assets/goods_image/img1.png'
  import img2 from '../assets/goods_image/img2.png'
  import img3 from '../assets/goods_image/img3.png'
  export default {
    name: 'WeShop',
    data () {
      return {
        msg: 'Welcome to Your Vue.js App',
        goodsList: [
          {id: 0, img_url: img1, radio_name: '1', radio_text: '景田'},
          {id: 1, img_url: img2, radio_name: '2', radio_text: '怡宝'},
          {id: 2, img_url: img3, radio_name: '3', radio_text: '仙谷'}
        ],
        radioSelected: '1'
      }
    },
    methods: {
      reverseMessage: function (radioName) {
        this.radioSelected = radioName
      },
      chooseAddress: function () {
        this.$router.push({ path: '/address' })
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
