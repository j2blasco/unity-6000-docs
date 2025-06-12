* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.Evaluate.html

#  [SphericalHarmonicsL2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.html).Evaluate
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
public void Evaluate(Vector3[] directions, Color[] results); 
### Parameters
Parameter | Description  
---|---  
directions | Array of normalized directions in which to evaluate the spherical harmonics.  
results | Output array for the evaluated values. The order of the results is the same as the directions array.  
### Description
Evaluates the spherical harmonics for each given direction. The `directions` and `results` arrays must have the same size.
```
using System.Collections;
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        UnityEngine.Rendering.SphericalHarmonicsL2 sh2;
        LightProbes.GetInterpolatedProbe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.GetInterpolatedProbe.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 0.0f, 0.0f), null, out sh2);  
  
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] directions = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[]
        {
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 1.0f, 0.0f),
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, -1.0f, 0.0f)
        };
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] results = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[2];  
  
        sh2.Evaluate(directions, results);
    }
}

```

* * *
