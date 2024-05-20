import { createClient } from "@gradio/client";

async function greet(name) {
    const app = await createClient("http://127.0.0.1:7860/");
    const result = await app.predict("/greet", [name]);
    console.log(result.data);
    return result.data;
}

export { greet };