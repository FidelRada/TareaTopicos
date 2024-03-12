// generateRoutes.js
const express = require('express');
//const { GPT } = require('@openai/gpt-3');
const { OpenAI } = require('openai');
const router = express.Router();

const openai = new OpenAI({ apiKey: myAPIKWY});

router.get('/', (req, res)=>{
    console.log("hola")
    res.json("hola")
})

router.post('/traducir', async (req, res) => {
    try {
        //console.log(req.body);
        const { msg } = req.body;
        //console.log(msg)

        const completion = await openai.chat.completions.create({
            model: "gpt-3.5-turbo",
            messages: [
              {
                "role": "system",
                "content": "Se te proporcionará una frase en español, y tu tarea es traducirla al inglés."
              },
              {
                "role": "user",
                //"content": "hola como esta tu mamá"
                "content": `${msg}`
              }
            ],

            max_tokens: 100
          });;

          response=completion.choices[0].message
        console.log(msg, response)
        res.json({response});
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

module.exports = router;
