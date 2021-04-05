<template>
    <v-card>
        <v-img
            height="200px"
            :src="require('../assets/images/night-sky.jpeg')"
            blur="2px"
        >
            <v-toolbar
                flat
                color="rgba(0,0,0,0)"
            >
                <v-toolbar-title class="title white--text pl-0">Welcome back, {{user.firstname}}!</v-toolbar-title>
            </v-toolbar>
        </v-img>
        <v-card-actions>
            <v-btn
                text
                @click="showEvents = !showEvents"
            >
                Your rentals
            </v-btn>
            <v-btn
                text
                @click="goToEvents"
            >
                Find an event
            </v-btn>
        </v-card-actions>
        <v-card-text v-if="showEvents">
            <div class="font-weight-bold ml-8 mb-2">
                Today
            </div>
            <v-timeline
                align-top
                dense
            >
                <v-timeline-item
                    v-for="event in userEvents"
                    :key="new Date(event.start)"
                    :color="event.color"
                    small
                >
                    <div>
                        <div class="font-weight-normal"><strong>{{event.name}}</strong></div>
                        <div>{{event.start}}</div>
                    </div>
                </v-timeline-item>
            </v-timeline>
        </v-card-text>
    </v-card>
</template>

<script>
    export default {
        name: "UserInfo",

        data: () => {
            return {
                user: {
                    firstname: "John",
                },
                userEvents: [
                    {
                        name: 'Test Event',
                        details: 'This is an event to test my code',
                        color: 'blue',
                        start: '2021-03-23 12:30',
                        end: '2021-03-23 13:30',
                    },
                    {
                        name: 'Test Event 2',
                        details: 'This is another event to test my code',
                        color: 'red',
                        start: '2021-03-23 14:30',
                        end: '2021-03-23 16:30',
                    },
                ],
                showEvents: false,
            }
        },

        methods: {
            goToEvents() {
                this.$router.push('/events', () => {});
            },
        }
    }
</script>

<style scoped>

</style>