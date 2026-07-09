import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  hcp_name: "",
  interaction_type: "",
  interaction_date: "",
  interaction_time: "",
  attendees: "",
  topics_discussed: "",
  sentiment: "",
  outcomes: "",
  follow_up_actions: "",
  materials: [],
  samples: [],
  followups: [],
  loading: false,
  error: null,
};

const interactionSlice = createSlice({
  name: "interaction",
  initialState,
  reducers: {
    setInteraction(state, action) {
      return {
        ...state,
        ...action.payload,
        loading: false,
        error: null,
      };
    },

    updateInteraction(state, action) {
      Object.assign(state, action.payload);
    },

    clearInteraction() {
      return initialState;
    },

    setLoading(state, action) {
      state.loading = action.payload;
    },

    setError(state, action) {
      state.error = action.payload;
      state.loading = false;
    },
  },
});

export const {
  setInteraction,
  updateInteraction,
  clearInteraction,
  setLoading,
  setError,
} = interactionSlice.actions;

export default interactionSlice.reducer;