* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume.html

# LightProbeProxyVolume
class in UnityEngine
/
Inherits from:[Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume.html "Go to LightProbeProxyVolume Component in the Manual")
### Description
The Light Probe Proxy Volume component offers the possibility to use higher resolution lighting for large non-static GameObjects.
By default, a probe-lit Renderer receives lighting from a single Light Probe that is interpolated from the surrounding Light Probes in the Scene. Because of this, GameObjects have constant ambient lighting regardless of their position on the surface. The light has have a rotational gradient because it's using spherical harmonics, but it lacks a spatial gradient. This is more noticeable on larger GameObjects and Particle Systems. The lighting across the GameObject matches the lighting at the anchor point, and if the GameObject straddles a lighting gradient, parts of the GameObject will look incorrect.  
  
This component will generate a 3D grid of interpolated Light Probes inside a bounding volume. The resolution of the grid can be user-specified. The spherical harmonics coefficients of the interpolated Light Probes are updated into 3D textures, which are sampled at render time to compute the contribution to the diffuse ambient lighting. This adds a spatial gradient to probe-lit GameObjects.  
  
Additional resources: [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html).
### Static Properties
Property | Description  
---|---  
[isFeatureSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume-isFeatureSupported.html) | Checks if Light Probe Proxy Volumes are supported.  
### Properties
Property | Description  
---|---  
[boundingBoxMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume-boundingBoxMode.html) | The bounding box mode for generating the 3D grid of interpolated Light Probes.  
[boundsGlobal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume-boundsGlobal.html) | The world-space bounding box in which the 3D grid of interpolated Light Probes is generated.  
[dataFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume-dataFormat.html) | The texture data format used by the Light Probe Proxy Volume 3D texture.  
[gridResolutionX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume-gridResolutionX.html) | The 3D grid resolution on the x-axis.  
[gridResolutionY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume-gridResolutionY.html) | The 3D grid resolution on the y-axis.  
[gridResolutionZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume-gridResolutionZ.html) | The 3D grid resolution on the z-axis.  
[originCustom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume-originCustom.html) | The local-space origin of the bounding box in which the 3D grid of interpolated Light Probes is generated.  
[probeDensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume-probeDensity.html) | Interpolated Light Probe density.  
[probePositionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume-probePositionMode.html) | The mode in which the interpolated Light Probe positions are generated.  
[qualityMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume-qualityMode.html) | Determines how many Spherical Harmonics bands will be evaluated to compute the ambient color.  
[refreshMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume-refreshMode.html) | Sets the way the Light Probe Proxy Volume refreshes.  
[resolutionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume-resolutionMode.html) | The resolution mode for generating the grid of interpolated Light Probes.  
[sizeCustom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume-sizeCustom.html) | The size of the bounding box in which the 3D grid of interpolated Light Probes is generated.  
### Public Methods
Method | Description  
---|---  
[Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume.Update.html) | Triggers an update of the Light Probe Proxy Volume.  
### Inherited Members
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-enabled.html) | Enabled Behaviours are Updated, disabled Behaviours are not.  
[isActiveAndEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html) | Reports whether a GameObject and its associated Behaviour is active and enabled.  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[BroadcastMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.BroadcastMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object or any of its children.  
[CompareTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.CompareTag.html) | Checks the GameObject's tag against the defined tag.  
[GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) | Gets a reference to a component of type T on the same GameObject as the component specified.  
[GetComponentInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInChildren.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any child of the GameObject.  
[GetComponentIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentIndex.html) | Gets the index of the component on its parent GameObject.  
[GetComponentInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInParent.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any parent of the GameObject.  
[GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponents.html) | Gets references to all components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInChildren.html) | Gets references to all components of type T on the same GameObject as the component specified, and any child of the GameObject.  
[GetComponentsInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInParent.html) | Gets references to all components of type T on the same GameObject as the component specified, and any parent of the GameObject.  
[SendMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object.  
[SendMessageUpwards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessageUpwards.html) | Calls the method named methodName on every MonoBehaviour in this game object and on every ancestor of the behaviour.  
[TryGetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.TryGetComponent.html) | Gets the component of the specified type, if it exists.  
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
