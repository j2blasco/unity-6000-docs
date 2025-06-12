* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullMode.html

# CullMode
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
Determines which faces Unity culls.
The following example shows how to use this enum to set the culling mode of a GameObject from a C# script.  
  
Use the following code in your shader to declare the `_Cull` property that you can change from a C# script:
```
                        Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) "Example/SetCullMode"
                        {
                            Properties
                            {
                                [Enum(UnityEngine.Rendering.CullMode)] _Cull ("Cull", Integer) = 1
                            }
                            SubShader
                            {
                                Cull [_Cull]
                                // Insert your shader code here
                            }
                        }

```

In a C# script, use the following code to change the `CullMode` property:
```
                        public void SetCullMode()
                        {
                            _material.SetInteger("_Cull", (int)UnityEngine.Rendering.CullMode.Back);
                        }

```

### Properties
Property | Description  
---|---  
[Off](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullMode.Off.html) | Disable culling.  
[Front](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullMode.Front.html) | Cull front-facing geometry.  
[Back](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullMode.Back.html) | Cull back-facing geometry.  
* * *
