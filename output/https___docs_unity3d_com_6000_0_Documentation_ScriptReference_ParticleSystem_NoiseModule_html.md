* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule.html

# NoiseModule
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
Script interface for the NoiseModule.
The Noise Module allows you to apply turbulence to the movement of your particles. Use the low quality settings to create computationally efficient Noise, or simulate smoother, richer Noise with the higher quality settings. You can also choose to define the behavior of the Noise individually for each axis.  
  
Additional resources: [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html), [ParticleSystem.noise](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-noise.html).
### Properties
Property | Description  
---|---  
[damping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-damping.html) | Higher frequency noise reduces the strength by a proportional amount, if enabled.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-enabled.html) | Specifies whether the the NoiseModule is enabled or disabled.  
[frequency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-frequency.html) | Low values create soft, smooth noise, and high values create rapidly changing noise.  
[octaveCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-octaveCount.html) | Layers of noise that combine to produce final noise.  
[octaveMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-octaveMultiplier.html) | When combining each octave, scale the intensity by this amount.  
[octaveScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-octaveScale.html) | When combining each octave, zoom in by this amount.  
[positionAmount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-positionAmount.html) | How much the noise affects the particle positions.  
[quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-quality.html) | Generate 1D, 2D or 3D noise.  
[remap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-remap.html) | Define how the noise values are remapped.  
[remapEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-remapEnabled.html) | Enable remapping of the final noise values, allowing for noise values to be translated into different values.  
[remapMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-remapMultiplier.html) | Remap multiplier.  
[remapX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-remapX.html) | Define how the noise values are remapped on the x-axis, when using the ParticleSystem.NoiseModule.separateAxes option.  
[remapXMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-remapXMultiplier.html) | x-axis remap multiplier.  
[remapY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-remapY.html) | Define how the noise values are remapped on the y-axis, when using the ParticleSystem.NoiseModule.separateAxes option.  
[remapYMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-remapYMultiplier.html) | y-axis remap multiplier.  
[remapZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-remapZ.html) | Define how the noise values are remapped on the z-axis, when using the ParticleSystem.NoiseModule.separateAxes option.  
[remapZMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-remapZMultiplier.html) | z-axis remap multiplier.  
[rotationAmount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-rotationAmount.html) | How much the noise affects the particle rotation, in degrees per second.  
[scrollSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-scrollSpeed.html) | Scroll the noise map over the Particle System.  
[scrollSpeedMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-scrollSpeedMultiplier.html) | Scroll speed multiplier.  
[separateAxes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-separateAxes.html) | Control the noise separately for each axis.  
[sizeAmount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-sizeAmount.html) | How much the noise affects the particle sizes, applied as a multiplier on the size of each particle.  
[strength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-strength.html) | How strong the overall noise effect is.  
[strengthMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-strengthMultiplier.html) | Strength multiplier.  
[strengthX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-strengthX.html) | Define the strength of the effect on the x-axis, when using the ParticleSystem.NoiseModule.separateAxes option.  
[strengthXMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-strengthXMultiplier.html) | x-axis strength multiplier.  
[strengthY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-strengthY.html) | Define the strength of the effect on the y-axis, when using the ParticleSystem.NoiseModule.separateAxes option.  
[strengthYMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-strengthYMultiplier.html) | y-axis strength multiplier.  
[strengthZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-strengthZ.html) | Define the strength of the effect on the z-axis, when using the ParticleSystem.NoiseModule.separateAxes option.  
[strengthZMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.NoiseModule-strengthZMultiplier.html) | z-axis strength multiplier.  
* * *
