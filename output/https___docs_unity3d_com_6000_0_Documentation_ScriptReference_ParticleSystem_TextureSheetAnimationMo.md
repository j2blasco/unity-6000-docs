* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule.html

# TextureSheetAnimationModule
struct in UnityEngine
/
Implemented in:[UnityEngine.ParticleSystemModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.ParticleSystemModule.html)
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html "Go to ParticleSystem Component in the Manual")
### Description
Script interface for the TextureSheetAnimationModule.
This module allows you to add animations to your particle textures. To author an animation, you must use a flipbook Texture.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ParticleFlipbook.png)  
_A flipbook texture sheet that contains eight sub-images of the numbers 1-8 across two rows of four columns. The first row contains the numbers 1-4 and the second row contains the numbers 5-8._  
  
Each numbered region represents a frame of the animation, which you must distribute evenly across the Texture. Select a variable below to see script examples. You may want to use this Texture on your Particle System with each example, to see how the module works.  
  
Additional resources: [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html), [ParticleSystem.textureSheetAnimation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-textureSheetAnimation.html).
### Properties
Property | Description  
---|---  
[animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-animation.html) | Specifies the animation type.  
[cycleCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-cycleCount.html) | Specifies how many times the animation loops during the lifetime of the particle.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-enabled.html) | Specifies whether the TextureSheetAnimationModule is enabled or disabled.  
[fps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-fps.html) | Control how quickly the animation plays.  
[frameOverTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-frameOverTime.html) | A curve to control which frame of the Texture sheet animation to play.  
[frameOverTimeMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-frameOverTimeMultiplier.html) | The frame over time mutiplier.  
[mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-mode.html) | Select whether the animated Texture information comes from a grid of frames on a single Texture, or from a list of Sprite objects.  
[numTilesX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-numTilesX.html) | Defines the tiling of the Texture in the x-axis.  
[numTilesY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-numTilesY.html) | Defines the tiling of the texture in the y-axis.  
[rowIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-rowIndex.html) | Explicitly select which row of the Texture sheet to use. The system uses this property when ParticleSystem.TextureSheetAnimationModule.rowMode is set to Custom.  
[rowMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-rowMode.html) | Select how particles choose which row of a Texture Sheet Animation to use.  
[speedRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-speedRange.html) | Specify how particle speeds are mapped to the animation frames.  
[spriteCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-spriteCount.html) | The total number of sprites.  
[startFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-startFrame.html) | Define a random starting frame for the Texture sheet animation.  
[startFrameMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-startFrameMultiplier.html) | The starting frame multiplier.  
[timeMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-timeMode.html) | Select whether the system bases the playback on mapping a curve to the lifetime of each particle, by using the particle speeds, or if playback simply uses a constant frames per second.  
[uvChannelMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule-uvChannelMask.html) | Choose which UV channels receive Texture animation.  
### Public Methods
Method | Description  
---|---  
[AddSprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule.AddSprite.html) | Add a new Sprite.  
[GetSprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule.GetSprite.html) | Get the Sprite at the given index.  
[RemoveSprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule.RemoveSprite.html) | Remove a Sprite from the given index in the array.  
[SetSprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule.SetSprite.html) | Set the Sprite at the given index.  
* * *
