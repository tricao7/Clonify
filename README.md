# VoiceCloning

VoiceCloning is a program that can clone voices and apply them to narration and text to speech.

- Generative AI for vocal cloning enhances customization in gaming and media by offering personalized audio.
- This technology augments text-to-speech models, enabling efficient production of NPC voices cutting costs for businesses.
- Adds more personalization to promote an immersive experience for users.

## Table of Contents

1. [Quickstart](#quickstart)
2. [Usage](#usage)
3. [Upcoming](#upcoming)  
4. [Conclusion](#conclusion)
5. [References](#references)

## Quickstart

Access the Web-Application. ([To Application](http://34.125.211.65/))

- Upload your own audio.
- Provide desired content for text-to-speech (TTS) model.
- Adjust various parameters for more customizability.

## Usage

[MetaVoice's](https://github.com/metavoiceio/metavoice-src/tree/main?tab=readme-ov-file) Text-To-Speech model takes text and a reference voice to fit the voice to the desired text. The reference voice is a 30 second passage reading the following script:

*"The North Wind and the Sun were disputing which was the stronger, when a traveler came along wrapped in a warm cloak. They agreed that the one who first succeeded in making the traveler take his cloak off should be considered stronger than the other. Then the North Wind blew as hard as he could, but the more he blew the more closely did the traveler fold his cloak around him; and at last the North Wind gave up the attempt. Then the Sun shined out warmly, and immediately the traveler took off his cloak.
And so the North Wind was obliged to confess that the Sun was the stronger of the two."*

<!DOCTYPE html>
<html>
    <body>
        <center>
            <p>Context/Reference Audio Example:</p>
            <figure>
                <audio controls src="./sample/sample_input.wav"></audio>
            </figure>
            <p>VoiceCloning Generated Audio Example with the following text content:</p>
            <ul>
                <li>"Let me generate a piece of text to see if my voice is easily replicable. If it's easy then it should be pretty accurate, otherwise I'm a bum."</li>
            </ul>
            <figure>
                <audio controls src="./sample/sample_output.wav"></audio>
            </figure>
        </center>
    </body>
</html>

## Upcoming

- [x] Customizable parameters to vary output.
- [ ] Better and faster inference with less reference data.
- [ ] Expand generated audio duration.

## Conclusion

In short, our VoiceCloning platform will allow our clients to

- Save on development budget.
- Provide a unique immersive experience to users.
- Shift recources to other dire projects.

## References

1. [metavoice](https://github.com/metavoiceio/metavoice-src/tree/main)
