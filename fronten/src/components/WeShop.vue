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

    <van-row>
      <van-col span="8">
        <van-stepper v-model="stepper1" />
      </van-col>
      <van-col span="8">

      </van-col>
      <van-col span="8">

      </van-col>
    </van-row>


    <van-button type="primary" @click="chooseAddress">提交订单</van-button>
    <van-picker :columns="pickerColumns" @change="handlePickerChange"></van-picker>
  </div>
</template>

<script>
  import img1 from '../assets/goods_image/img1.png'
  import img2 from '../assets/goods_image/img2.png'
  import img3 from '../assets/goods_image/img3.png'

  const citys = {
    '浙江': ['杭州', '宁波', '温州', '嘉兴', '湖州', '绍兴', '金华', '衢州', '舟山', '台州', '丽水'],
    '福建': ['福州', '厦门', '莆田', '三明', '泉州', '漳州', '南平', '龙岩', '宁德'],
    '湖南': ['长沙', '株洲', '湘潭', '衡阳', '邵阳', '岳阳', '常德', '张家界', '益阳', '郴州', '永州', '怀化', '娄底', '湘西土家族苗族自治州']
  }

  export default {
    name: 'WeShop',
    data () {
      return {
        msg: 'Welcome to Your Vue.js App',
        goodsList: [
          {id: 0, img_url: img1, radio_name: '1', radio_text: '商品A'},
          {id: 1, img_url: img2, radio_name: '2', radio_text: '商品B'},
          {id: 2, img_url: img3, radio_name: '3', radio_text: '商品C'}
        ],
        radioSelected: '1',
        pickerColumns: [
          {
            values: Object.keys(citys),
            className: 'column1'
          },
          {
            values: ['杭州', '宁波', '温州', '嘉兴', '湖州', '绍兴', '金华', '衢州', '舟山', '台州', '丽水'],
            className: 'column2'
          }
        ]
      }
    },
    methods: {
      reverseMessage: function (radioName) {
        this.radioSelected = radioName
      },
      chooseAddress: function () {
        this.$router.push({ path: '/address' })
      },
      handlePickerChange (picker, values) {
        picker.setColumnValues(1, citys[values[0]])
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
