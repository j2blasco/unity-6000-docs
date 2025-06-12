* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings.html

# RenderSettings
class in UnityEngine
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
The Render Settings contain values for a range of visual elements in your Scene, like fog and ambient light.
Note that render settings are per-scene.
### Static Properties
Property | Description  
---|---  
[ambientEquatorColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientEquatorColor.html) | Ambient lighting coming from the sides.  
[ambientGroundColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientGroundColor.html) | Ambient lighting coming from below.  
[ambientIntensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientIntensity.html) | How much the light from the Ambient Source affects the Scene.  
[ambientLight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientLight.html) | Flat ambient lighting color.  
[ambientMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientMode.html) | Ambient lighting mode.  
[ambientProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientProbe.html) | An ambient probe that captures environment lighting.  
[ambientSkyColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientSkyColor.html) | Ambient lighting coming from above.  
[defaultReflectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-defaultReflectionMode.html) | Default reflection mode.  
[defaultReflectionResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-defaultReflectionResolution.html) | Cubemap resolution for default reflection.  
[flareFadeSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-flareFadeSpeed.html) | The fade speed of all flares in the Scene.  
[flareStrength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-flareStrength.html) | The intensity of all flares in the Scene.  
[fog](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fog.html) | Is fog enabled?  
[fogColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fogColor.html) | The color of the fog.  
[fogDensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fogDensity.html) | The density of the exponential fog.  
[fogEndDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fogEndDistance.html) | The ending distance of linear fog.  
[fogMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fogMode.html) | Fog mode to use.  
[fogStartDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fogStartDistance.html) | The starting distance of linear fog.  
[haloStrength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-haloStrength.html) | Size of the Light halos.  
[reflectionBounces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-reflectionBounces.html) | The number of times a reflection includes other reflections.  
[reflectionIntensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-reflectionIntensity.html) | How much the skybox / custom cubemap reflection affects the Scene.  
[skybox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-skybox.html) | The global skybox to use.  
[subtractiveShadowColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-subtractiveShadowColor.html) | The color used for the sun shadows in the Subtractive lightmode.  
[sun](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-sun.html) | The light used by the procedural skybox.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
