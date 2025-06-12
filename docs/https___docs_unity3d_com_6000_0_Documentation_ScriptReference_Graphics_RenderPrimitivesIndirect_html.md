* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitivesIndirect.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).RenderPrimitivesIndirect
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
public static void RenderPrimitivesIndirect(ref [RenderParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html) rparams, [MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html) topology, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) commandBuffer, int commandCount = 1, int startCommand = 0); 
### Parameters
Parameter | Description  
---|---  
rparams | The parameters Unity uses to render the primitives.  
topology | Primitive topology (for example, triangles or lines).  
commandBuffer | A command buffer that provides rendering command arguments (see [IndirectDrawArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.IndirectDrawArgs.html)).  
commandCount | The number of rendering commands to execute in the `commandBuffer`.  
startCommand | The first command to execute in the `commandBuffer`.  
### Description
Renders primitives with GPU instancing and a custom shader using rendering command arguments from `commandBuffer`.
This function provides a way to control rendering command arguments from GPU to render a given number of primitives and instances. Use `RenderParams.worldBounds` to define bounds to cull and sort the geometry rendered with the method as a single entity.  
  
This function only works on platforms that support [compute shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html).  
  
Add the following lines in the pass section of a shader to access command, instance and vertex ID's as specified in UnityIndirect.cginc: Additional resources: [RenderMeshIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshIndirect.html).
```
#define UNITY_INDIRECT_DRAW_ARGS IndirectDrawArgs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.IndirectDrawArgs.html)
#include "UnityIndirect.cginc"
```

Add the following line to the beginning of a shader function to setup the ID access functions:
```
InitIndirectDrawArgs(0); // pass SV_DrawID semantic value here for multi-draw support
```

The following example executes two indirect rendering commands. Each command renders 10 Mesh instances. The associated Material must use the below custom shader:
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material;
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh;  
  
    GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) meshTriangles;
    GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) meshPositions;
    GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) commandBuf;
    GraphicsBuffer.IndirectDrawArgs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.IndirectDrawArgs.html)[] commandData;
    const int commandCount = 2;  
  
    void Start()
    {
        // note: remember to check "Read/Write" on the mesh asset to get access to the geometry data
        meshTriangles = new GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html)(GraphicsBuffer.Target.Structured[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Structured.html), mesh.triangles.Length, sizeof(int));
        meshTriangles.SetData(mesh.triangles);
        meshPositions = new GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html)(GraphicsBuffer.Target.Structured[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Structured.html), mesh.vertices.Length, 3 * sizeof(float));
        meshPositions.SetData(mesh.vertices);
        commandBuf = new GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html)(GraphicsBuffer.Target.IndirectArguments[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.IndirectArguments.html), commandCount, GraphicsBuffer.IndirectDrawArgs.size[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.IndirectDrawArgs-size.html));
        commandData = new GraphicsBuffer.IndirectDrawArgs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.IndirectDrawArgs.html)[commandCount];
    }  
  
    void OnDestroy()
    {
        meshTriangles?.Dispose();
        meshTriangles = null;
        meshPositions?.Dispose();
        meshPositions = null;
        commandBuf?.Dispose();
        commandBuf = null;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        RenderParams[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html) rp = new RenderParams[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html)(material);
        rp.worldBounds = new Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), 10000*Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html)); // use tighter bounds
        rp.matProps = new MaterialPropertyBlock[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html)();
        rp.matProps.SetBuffer("_Triangles", meshTriangles);
        rp.matProps.SetBuffer("_Positions", meshPositions);
        rp.matProps.SetInt("_BaseVertexIndex", (int)mesh.GetBaseVertex(0));
        rp.matProps.SetMatrix("_ObjectToWorld", Matrix4x4.Translate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Translate.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-4.5f, 0, 0)));
        commandData[0].vertexCountPerInstance = mesh.GetIndexCount(0);
        commandData[0].instanceCount = 10;
        commandData[1].vertexCountPerInstance = mesh.GetIndexCount(0);
        commandData[1].instanceCount = 10;
        commandBuf.SetData(commandData);
        Graphics.RenderPrimitivesIndirect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitivesIndirect.html)(rp, MeshTopology.Triangles[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.Triangles.html), commandBuf, commandCount);
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
            #define UNITY_INDIRECT_DRAW_ARGS IndirectDrawArgs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.IndirectDrawArgs.html)
            #include "UnityIndirect.cginc"  
  
            struct v2f
            {
                float4 pos : SV_POSITION;
                float4 color : COLOR0;
            };  
  
            StructuredBuffer<int> _Triangles;
            StructuredBuffer<float3> _Positions;
            uniform uint _BaseVertexIndex;
            uniform float4x4 _ObjectToWorld;  
  
            v2f vert(uint svVertexID: SV_VertexID, uint svInstanceID : SV_InstanceID)
            {
                InitIndirectDrawArgs(0);
                v2f o;
                uint cmdID = GetCommandID(0);
                uint instanceID = GetIndirectInstanceID(svInstanceID);
                float3 pos = _Positions[_Triangles[GetIndirectVertexID(svVertexID)] + _BaseVertexIndex];
                float4 wpos = mul(_ObjectToWorld, float4(pos + float3(instanceID, cmdID, 0.0f), 1.0f));
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
