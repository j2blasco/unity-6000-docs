* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ResetPreMappedBufferMemory.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).ResetPreMappedBufferMemory
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
## Declaration
public static void ResetPreMappedBufferMemory(); 
### Description
Reset the cache of reserved graphics memory used for efficient rendering of Particle Systems.
In order to efficiently write its data into graphics memory, the Particle System uses a pool of pre-allocated vertex buffers. When rendering a large number of particles, this pool will increase in size, and then maintain this size even when rendering fewer particles afterwards.  
  
Maintaining a large pool can make future rendering more efficient, in situations where a large number of particles are being rendered, and the pool is already pre-sized appropriately. However, a large pool uses more memory, so this function allows that memory to be released.  
  
This method is most useful when you know that you have finished rendering a high number of particles, and will not need to render a similar amount in the near future, i.e. when transitioning from a scene containing a large number of particles, to one where fewer particles will be rendered.  
  
Modern graphics APIs, such as DirectX12, Vulkan and Metal, do not use a pre-allocated pool of vertex buffers, because they can operate efficiently without it. This method does nothing on these devices.
* * *
