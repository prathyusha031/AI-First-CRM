import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  hcpName: "",
  interactionType: "",
  date: "",
  time: "",
  attendees: "",
  topics: "",
  materialsShared: [],
  samplesDistributed: [],
  sentiment: "",
  outcomes: "",
  followUp: "",
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