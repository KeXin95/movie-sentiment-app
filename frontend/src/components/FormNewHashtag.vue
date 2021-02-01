<template>
    <div>
        <b-form-textarea v-model="sentence" rows="8" no-resize id="textarea-default" placeholder="Type your sentence here..."></b-form-textarea>
        <b-button v-on:click="save" variant="primary" @click="hideinput ^= true">Check sentiment</b-button>
        <br/><br/>
        <h2 v-show="isShowing"> This sentence is <b>"{{value}}"</b></h2>
        <h2 align=left> Explanation on the prediction: </h2>
        <iframe :src="source" height="1000" width="950" frameborder=0></iframe>


    </div>
</template>

<script>
import axios from 'axios'
export default {
    name : 'FormNewHashtag',
    data() {
        return{
            sentence: this.hashtag,
            isShowing: false,
            isShowingHTML: false,
            value: "",
            value2: "",
            hideinput: false,
            source: 'http://192.168.1.19:8080/app/temp.html#/'
        }
    },
    methods :{
        save : function(){
            axios
                .get('http://127.0.0.1:5000/scan?sentence='+ this.sentence)
                .then(function (response) {
                    console.log(response);
                    this.isShowing = true;
                    this.inputsentence = this.sentence;
                    this.value = response['data']['result'];
                    this.$emit('childToParent', 2)
                }.bind(this))
                .catch(function (error) {
                    console.log(error);
                });
            axios
                .get('http://127.0.0.1:5000/explain?sentence='+ this.sentence)
                .then(function (response) {
                    console.log("waiting for explainer..")
                    console.log(response);
                    this.isShowingHTML = true;
                    this.value2 = response['data']['result'];
                }.bind(this))
                .catch(function (error) {
                    console.log(error);
                });
        }


    }
}
</script>