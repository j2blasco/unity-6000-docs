* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.OpaqueSortMode.html

# OpaqueSortMode
enumeration
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
### Description
Opaque object sorting mode of a [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).
Opaque objects are sorted by various criteria (sorting layers, shader queues, materials, distance, lightmaps etc.) to maximize both the CPU efficiency (reduce number of state changes and improve draw call batching), and to maximize GPU efficiency (many GPUs prefer rough front-to-back rendering order for faster rejection of invisible surfaces).  
  
By default, opaque objects are grouped in rough front-to-back buckets, on the GPUs where doing that is beneficial. There are GPUs where doing this distance based sorting is not really helpful (most notably, PowerVR/Apple GPUs), and so on these GPUs the distance based sorting is not done by default.  
  
The [Camera.opaqueSortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-opaqueSortMode.html) property lets you override this default behavior. For example, you might want to never do distance-based sorting for opaque objects, if you know you need much more CPU performance than GPU performance.  
  
Additional resources: [Camera.opaqueSortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-opaqueSortMode.html).
### Properties
Property | Description  
---|---  
[Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.OpaqueSortMode.Default.html) | Default opaque sorting mode.  
[FrontToBack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.OpaqueSortMode.FrontToBack.html) | Do rough front-to-back sorting of opaque objects.  
[NoDistanceSort](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.OpaqueSortMode.NoDistanceSort.html) | Do not sort opaque objects by distance.  
* * *
