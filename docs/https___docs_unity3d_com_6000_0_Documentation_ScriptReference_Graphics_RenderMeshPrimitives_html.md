* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshPrimitives.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).RenderMeshPrimitives
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
public static void RenderMeshPrimitives(ref [RenderParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html) rparams, [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, int submeshIndex, int instanceCount = 1); 
### Parameters
Parameter | Description  
---|---  
rparams | The parameters Unity uses to render the Mesh primitives.  
mesh | The [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) to render.  
submeshIndex | The index of a submesh Unity renders when the Mesh contains multiple Materials (submeshes). For a Mesh with a single Material, use value 0.  
instanceCount | The number of instances to render.  
### Description
Renders multiple instances of a Mesh using GPU instancing and a custom shader.
This method renders multiple instances of the same Mesh, similar to [Graphics.RenderMeshIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshIndirect.html), but provides the number of instances and other rendering command arguments as function arguments.  
  
Use `SV_InstanceID` semantic in shaders to access the rendered instance.  
  
The following example uses `RenderMeshPrimitives` to render 10 Mesh instances. The associated Material must use the below custom shader:
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material;
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        RenderParams[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html) rp = new RenderParams[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html)(material);
        rp.worldBounds = new Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), 10000*Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html)); // use tighter bounds
        rp.matProps = new MaterialPropertyBlock[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html)();
        rp.matProps.SetMatrix("_ObjectToWorld", Matrix4x4.Translate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Translate.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-4.5f, 0, 0)));
        rp.matProps.SetFloat("_NumInstances", 10.0f);
        Graphics.RenderMeshPrimitives[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshPrimitives.html)(rp, mesh, 0, 10);
    }
}
```

Use the following example shader with the above C# example code:
```
          Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) "ExampleShader"
{
    SubShader
    {
        Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html)
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag  
  
            #include "UnityCG.cginc"  
  
            struct v2f
            {
                float4 pos : SV_POSITION;
                float4 color : COLOR0;
            };  
  
            uniform float4x4 _ObjectToWorld;
            uniform float _NumInstances;  
  
            v2f vert(appdata_base v, uint instanceID : SV_InstanceID)
            {
                v2f o;
                float4 wpos = mul(_ObjectToWorld, v.vertex + float4(instanceID, 0, 0, 0));
                o.pos = mul(UNITY_MATRIX_VP, wpos);
                o.color = float4(instanceID / _NumInstances, 0.0f, 0.0f, 0.0f);
                return o;
            }  
  
            float4 frag(v2f i) : SV_Target
            {
                return i.color;
            }
            ENDCG
        }
    }
}
```

* * *
