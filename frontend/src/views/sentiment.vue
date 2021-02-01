<template>
  <div class="hashtag">
    <b-container>
      <h1 class="text-left mt-3">Sentiment</h1>
      <hr />
      <b-row>
        <b-col cols="10">
          <div>
            <FormNewHashtag :hashtag="hashtag" v-on:childToParent="onChildClick" />
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import FormNewHashtag from "@/components/FormNewHashtag.vue";

export default {
  name: "Hashtag",
  data: function() {
    return {
      menu: 2,
      hashtag: null,
      id: null
    };
  },
  components: {
    FormNewHashtag: FormNewHashtag
  },
  methods: {
    onChildClick(value) {
      this.menu = value;
      this.hashtag = null;
    },
    actionButton(id, hashtag) {
      this.id = id;
      this.hashtag = hashtag;
      this.menu = 1;
    }
  }
};
</script>