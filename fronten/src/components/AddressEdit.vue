<template>
  <div>
    <van-button type="primary" @click="onBack">Primary</van-button>
    <van-address-edit
      :area-list="areaList"
      :show-postal="true"
      :show-set-default="true"
      :show-search-result="true"
      :search-result="searchResult"
      @save="onSave"
      @delete="onDelete"
      @change-detail="onChangeDetail"
    />
  </div>
</template>

<script>
  import AreaList from '../assets/AreaList.json'
  export default {
    data () {
      return {
        areaList: AreaList,
        searchResult: []
      }
    },

    methods: {
      onSave () {
//        Toast('save')
      },
      onDelete () {
//        Toast('delete')
      },
      onChangeDetail (val) {
        if (val) {
          this.searchResult = [{
            name: '黄龙万科中心',
            address: '杭州市西湖区'
          }]
        } else {
          this.searchResult = []
        }
      },
      onBack () {
        this.$router.push({ path: '/address' })
      }
    }
  }
</script>

<style scoped>

</style>
