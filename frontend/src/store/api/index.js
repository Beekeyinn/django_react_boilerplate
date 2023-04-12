import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

const stableAPI = createApi({
  reducerPath: "stableAPI",
  baseQuery: fetchBaseQuery({
    baseUrl: "",
  }),
  tagTypes: ["images"],
  endpoints: (builder) => ({
    stabilityImages: builder.mutation({
      query: (body) => ({
        url: "/",
        method: "POST",
        body: body,
      }),
      invalidatesTags: ["images"],
    }),
  }),
});

export default stableAPI;
export const { useStabilityImagesMutation } = stableAPI;
