import { configureStore, getDefaultMiddleware } from "@reduxjs/toolkit";
import stableAPI from "./api";

const store = configureStore({
  reducer: {
    [stableAPI.reducerPath]: stableAPI.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(stableAPI.middleware),
});

export default store;
