* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.PopulateWorld.html

#  [InputExtraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.html).PopulateWorld
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
## Declaration
public static bool PopulateWorld([LightTransport.InputExtraction.BakeInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.BakeInput.html) bakeInput, [LightTransport.BakeProgressState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BakeProgressState.html) progress, [LightTransport.IDeviceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.html) context, [LightTransport.IWorld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IWorld.html) world); 
### Parameters
Parameter | Description  
---|---  
bakeInput | The bake input to use.  
progress | Progress tracker.  
context | Device context.  
world | The world to populate with the contents of the bake input.  
### Returns
**bool** True if the world was populated successfully. 
### Description
Populate the given world from a bake input.
This method generates the world space data structures used by integrators. For example, acceleration structures, lookup tables, and other data structures that can be shared between integrators. Related content: [IWorld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IWorld.html).
```
How to populate a world from a bake input.
```

// Extract bake input. bool result = UnityEngine.LightTransport.InputExtraction.ExtractFromScene(out var input); Assert.IsTrue(result);  
  
// Create context and world. var context = new RadeonRaysContext(); Assert.NotNull(context);  
  
var contextInitialized = context.Initialize(); Assert.AreEqual(true, contextInitialized); var world = new RadeonRaysWorld();  
  
// Populate the integration world. using var progress = new BakeProgressState(); var worldResult = UnityEngine.LightTransport.InputExtraction.PopulateWorld(input, progress, context, world); Assert.IsTrue(worldResult);  
  
Context.Dispose();
* * *
