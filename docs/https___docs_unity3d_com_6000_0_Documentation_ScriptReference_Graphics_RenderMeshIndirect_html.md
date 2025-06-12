* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshIndirect.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).RenderMeshIndirect
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
public static void RenderMeshIndirect(ref [RenderParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html) rparams, [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) commandBuffer, int commandCount = 1, int startCommand = 0); 
### Parameters
Parameter | Description  
---|---  
rparams | The parameters Unity uses to render the mesh.  
mesh | The [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) to render.  
commandBuffer | A command buffer that provides rendering command arguments (see [IndirectDrawIndexedArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.IndirectDrawIndexedArgs.html)).  
commandCount | The number of rendering commands to execute in the `commandBuffer`.  
startCommand | The first command to execute in the `commandBuffer`.  
### Description
Renders multiple instances of a mesh using GPU instancing and rendering command arguments from `commandBuffer`.
This function renders multiple instances of the same Mesh, similar to [Graphics.RenderMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshInstanced.html), but takes the rendering command arguments from `commandBuffer`. You can set up these command arguments with either the CPU or the GPU. The `commandBuffer` can contain multiple rendering commands that you can execute with a single call to this method. On supported platforms Unity may further optimize CPU performance of multi-command calls by submitting a single multi-draw rendering command to the low-level API. Use [IndirectDrawIndexedArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.IndirectDrawIndexedArgs.html) to setup the command buffer (instead of plain ints) as the layout of this structure can change depending on the platform.  
  
This function only works on platforms that support [compute shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html).  
  
Use this function to draw the same Mesh multiple times times using a custom shader and GPU controlled rendering arguments. Use `RenderParams.worldBounds` to define bounds to cull and sort the geometry rendered with the method as a single entity..  
  
Add the following lines in the pass section of a shader to access command, instance and vertex ID's as specified in UnityIndirect.cginc:
```
#define UNITY_INDIRECT_DRAW_ARGS IndirectDrawIndexedArgs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.IndirectDrawIndexedArgs.html)
#include "UnityIndirect.cginc"
```

Add the following line to the beginning of the shader function to setup the ID access functions:
```
InitIndirectDrawArgs(0); // pass SV_DrawID semantic value here for multi-draw support
```

Additional resources: [RenderMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshInstanced.html).  
  
The following example executes two indirect rendering commands. Each command renders 10 Mesh instances. The associated Material must use the below custom shader:
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material;
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh;  
  
    GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) commandBuf;
    GraphicsBuffer.IndirectDrawIndexedArgs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.IndirectDrawIndexedArgs.html)[] commandData;
    const int commandCount = 2;  
  
    void Start()
    {
        commandBuf = new GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html)(GraphicsBuffer.Target.IndirectArguments[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.IndirectArguments.html), commandCount, GraphicsBuffer.IndirectDrawIndexedArgs.size[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.IndirectDrawIndexedArgs-size.html));
        commandData = new GraphicsBuffer.IndirectDrawIndexedArgs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.IndirectDrawIndexedArgs.html)[commandCount];
    }  
  
    void OnDestroy()
    {
        commandBuf?.Release();
        commandBuf = null;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        RenderParams[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html) rp = new RenderParams[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html)(material);
        rp.worldBounds = new Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), 10000*Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html)); // use tighter bounds for better FOV culling
        rp.matProps = new MaterialPropertyBlock[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html)();
        rp.matProps.SetMatrix("_ObjectToWorld", Matrix4x4.Translate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Translate.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-4.5f, 0, 0)));
        commandData[0].indexCountPerInstance = mesh.GetIndexCount(0);
        commandData[0].instanceCount = 10;
        commandData[1].indexCountPerInstance = mesh.GetIndexCount(0);
        commandData[1].instanceCount = 10;
        commandBuf.SetData(commandData);
        Graphics.RenderMeshIndirect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshIndirect.html)(rp, mesh, commandBuf, commandCount);
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
            #define UNITY_INDIRECT_DRAW_ARGS IndirectDrawIndexedArgs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.IndirectDrawIndexedArgs.html)
            #include "UnityIndirect.cginc"  
  
            struct v2f
            {
                float4 pos : SV_POSITION;
                float4 color : COLOR0;
            };  
  
            uniform float4x4 _ObjectToWorld;  
  
            v2f vert(appdata_base v, uint svInstanceID : SV_InstanceID)
            {
                InitIndirectDrawArgs(0);
                v2f o;
                uint cmdID = GetCommandID(0);
                uint instanceID = GetIndirectInstanceID(svInstanceID);
                float4 wpos = mul(_ObjectToWorld, v.vertex + float4(instanceID, cmdID, 0, 0));
                o.pos = mul(UNITY_MATRIX_VP, wpos);
                o.color = float4(cmdID & 1 ? 0.0f : 1.0f, cmdID & 1 ? 1.0f : 0.0f, instanceID / float(GetIndirectInstanceCount()), 0.0f);
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
