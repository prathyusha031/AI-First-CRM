import api from "./api";

export async function logInteraction(message) {
  const response = await api.post("/interactions/log", {
    message,
  });

  return response.data;
}