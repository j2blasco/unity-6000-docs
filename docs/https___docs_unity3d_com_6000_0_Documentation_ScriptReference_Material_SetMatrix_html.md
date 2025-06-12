* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetMatrix.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).SetMatrix
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html "Go to Material Component in the Manual")
## Declaration
public void SetMatrix(string name, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) value); 
## Declaration
public void SetMatrix(int nameID, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) value); 
### Parameters
Parameter | Description  
---|---  
nameID | Property name ID, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get it.  
name | Property name, e.g. "_CubemapRotation".  
value | Matrix value to set.  
### Description
Sets a named matrix for the shader.
This is mostly used with custom shaders that need extra matrix parameters. Matrix parameters are not exposed in the material inspector, but can be set and queried with `SetMatrix` and `GetMatrix` from scripts.  
  
Additional resources: [GetMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetMatrix.html), [Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html), [ShaderLab documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html), [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html), [Properties in Shader Programs](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PropertiesInPrograms.html).
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Attach to an object that has a Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) component,
    // and use material with the shader below.
    public float rotateSpeed = 30f;
    public void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Construct a rotation matrix and set it for the shader
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rot = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(0, 0, Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) * rotateSpeed);
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) m = Matrix4x4.TRS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.TRS.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), rot, Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html));
        GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>().material.SetMatrix("_TextureRotation", m);
    }
}

```

```
// Use this shader on an object together with the above example script.
// The shader transforms texture coordinates with a matrix set from a script.
Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) "RotatingTexture"
{
    Properties
    {
        _MainTex ("Base (RGB)", 2D) = "white" {}
    }
    SubShader
    {
        Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html)
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag  
  
            struct v2f
            {
                float2 uv : TEXCOORD0;
                float4 pos : SV_POSITION;
            };  
  
            float4x4 _TextureRotation;  
  
            v2f vert (float4 pos : POSITION, float2 uv : TEXCOORD0)
            {
                v2f o;
                o.pos = UnityObjectToClipPos(pos);
                o.uv = mul(_TextureRotation, float4(uv,0,1)).xy;
                return o;
            }  
  
            sampler2D _MainTex;
            fixed4 frag (v2f i) : SV_Target
            {
                return tex2D(_MainTex, i.uv);
            }
            ENDCG
        }
    }
}
```

* * *
