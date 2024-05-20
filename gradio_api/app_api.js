import { createClient } from "@gradio/client";

async function main() {
    const app = await createClient("http://127.0.0.1:7860/");
    const result = await app.predict("/greet", [		
        "jim ready!!", // string  in 'Name' Textbox component
    ]);

    console.log(result.data);
}

main();
