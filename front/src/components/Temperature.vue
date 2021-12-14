<template>
  <div class="container">
    <div class="row">

      <div class="col-3">
        <h1 class="row">Capteur 1</h1>
        <br>
        <vue-thermometer
      :value="temp1"
      :min="min"
      :max="max"/>
      <div class="mr-16">
       <v-slider
        class="align-center mr-16 mt-16"
        v-model="temp1"
        
        :min="min"
        :max="max"
         always-dirty
         :rules="rules"
         thumb-label="always"
      ></v-slider>
      </div>
      </div>

      <div class="col-3">
        <h1 class="row">Capteur 2</h1>
        <br>
        <vue-thermometer
      :value="temp2"
      :min="min"
      :max="max"
      />
      <div class="mr-16">
       <v-slider
        class="align-center mr-16 mt-16"
        v-model="temp2"
        
        :min="min"
        :max="max"
         always-dirty
         :rules="rules"
         thumb-label="always"
      ></v-slider>
      </div>
      </div>

    <div class="col-3">
        <h1 class="row">Capteur 3</h1>
        <br>
        <vue-thermometer
      :value="temp3"
      :min="min"
      :max="max"
      />
      <div class="mr-16">
       <v-slider
        class="align-center mr-16 mt-16"
        v-model="temp3"
        
        :min="min"
        :max="max"
         always-dirty
         :rules="rules"
         thumb-label="always"
      ></v-slider>
      </div>
      </div>
      </div>
  <div class="row align-center ma-16">
    <v-btn
      rounded
      color="primary"
      dark
       @click="postValues"
    >
      Save values
    </v-btn>
    <v-snackbar
      v-model="snackbar"
    >
      {{ text }}

      <template v-slot:action="{ attrs }">
        <v-btn
          color="pink"
          text
          v-bind="attrs"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      temp1: 20,
      temp2: 15,
      temp3: 10,
      min: 0,
      max: 60,
      rules: [
        v => v <= 60 && v > 0,
      ],
      text:"",
      snackbar:false,
    };
  },
  methods: {
    postValues() {
      const path = 'http://localhost:5000/';
      const payload={
        temp1:this.temp1,
        temp2:this.temp2,
        temp3:this.temp3,
        
      }
      axios.post(path, payload)
        .then((response) => {
          this.text = response.data.status
          this.snackbar = true
        })
        .catch((error) => {
          this.text = response.data.status
          this.snackbar = true
        });
    },
  },
  /*watch: {
      // whenever question changes, this function will run
      temp1(newTemp, oldTemp) {
        this.postValues()
      },
      temp2(newTemp, oldTemp) {
        this.postValues()     
      },
      temp3(newTemp, oldTemp) {
        this.postValues()
      }
    }*/
};
</script>
