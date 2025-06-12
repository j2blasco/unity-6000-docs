* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.html

# DrawCameraMode
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
Drawing modes for [Handles.DrawCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawCamera.html).
### Properties
Property | Description  
---|---  
[UserDefined](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.UserDefined.html) | A custom mode defined by the user.  
[Normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.Normal.html) | Draw the camera like it would be drawn in-game. This uses the clear flags of the camera.  
[Textured](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.Textured.html) | Draw the camera textured with selection wireframe and no background clearing.  
[Wireframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.Wireframe.html) | Draw the camera in wireframe and no background clearing.  
[TexturedWire](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.TexturedWire.html) | Draw the camera where all objects have a wireframe overlay. and no background clearing.  
[ShadowCascades](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.ShadowCascades.html) | The camera is set to draw directional light shadow map cascades.  
[RenderPaths](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.RenderPaths.html) | The camera is set to draw color coded render paths.  
[AlphaChannel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.AlphaChannel.html) | The camera is set to display the alpha channel of the rendering.  
[Overdraw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.Overdraw.html) | The camera is set to display Scene overdraw, with brighter colors indicating more overdraw.  
[Mipmaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.Mipmaps.html) | The camera is set to display the texture resolution, with a red tint indicating resolution that is too high, and a blue tint indicating texture sizes that could be higher.  
[DeferredDiffuse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.DeferredDiffuse.html) | Draw diffuse color of Deferred Shading G-buffer.  
[DeferredSpecular](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.DeferredSpecular.html) | Draw specular color of Deferred Shading G-buffer.  
[DeferredSmoothness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.DeferredSmoothness.html) | Draw smoothness value of Deferred Shading G-buffer.  
[DeferredNormal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.DeferredNormal.html) | Draw world space normal of Deferred Shading G-buffer.  
[RealtimeCharting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.RealtimeCharting.html) | Draw objects with different colors for each real-time chart (UV island).  
[Systems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.Systems.html) | Draw objects with different color for each GI system.  
[RealtimeAlbedo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.RealtimeAlbedo.html) | Draw objects with the Enlighten Realtime Global Illumination albedo component only.  
[RealtimeEmissive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.RealtimeEmissive.html) | Draw objects with the Enlighten Realtime Global Illumination emission component only.  
[RealtimeIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.RealtimeIndirect.html) | Draw objects with the Enlighten Realtime Global Illumination indirect light only.  
[RealtimeDirectionality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.RealtimeDirectionality.html) | Draw objects with the Enlighten Realtime Global Illumination directionality component only.  
[BakedLightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.BakedLightmap.html) | Draw objects with the baked lightmap only.  
[Clustering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.Clustering.html) | Draw with different colors for each cluster.  
[LitClustering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.LitClustering.html) | Draw lit clusters.  
[ValidateAlbedo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.ValidateAlbedo.html) | The camera is set to draw a physically based, albedo validated rendering.  
[ValidateMetalSpecular](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.ValidateMetalSpecular.html) | The camera is set to draw a physically based, metal or specular validated rendering.  
[ShadowMasks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.ShadowMasks.html) | The camera is set to display colored ShadowMasks, coloring light gizmo with the same color.  
[LightOverlap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.LightOverlap.html) | The camera is set to show in red static lights that fall back to 'static' because more than four light volumes are overlapping.  
[BakedAlbedo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.BakedAlbedo.html) | Draw objects with the baked albedo component only.  
[BakedEmissive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.BakedEmissive.html) | Draw objects with the baked emission component only.  
[BakedDirectionality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.BakedDirectionality.html) | Draw objects with the baked directionality component only.  
[BakedTexelValidity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.BakedTexelValidity.html) | Draw objects with baked texel validity only.  
[BakedIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.BakedIndices.html) | Draw objects with baked indices only.  
[BakedCharting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.BakedCharting.html) | Draw objects with different colors for each baked chart (UV island).  
[SpriteMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.SpriteMask.html) | The camera is set to display SpriteMask and SpriteRenderer with SpriteRenderer.maskInteraction set.  
[BakedUVOverlap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.BakedUVOverlap.html) | Draw objects with overlapping lightmap texels highlighted.  
[TextureStreaming](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.TextureStreaming.html) | The camera is set to run in texture streaming debug mode.  
[BakedLightmapCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.BakedLightmapCulling.html) | Draw objects with visible lightmap texels highlighted.  
[GIContributorsReceivers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.GIContributorsReceivers.html) | Draw Mesh Renderers and Terrains in different colors to show their StaticEditorFlags.ContributeGI / ReceiveGI properties. With default colors: Yellow means 'ContributeGI' is off. Blue means that 'ContributeGI' is on and the object receives GI from lightmaps. Additional resources: ReceiveGI.Lightmaps Red means that 'ContributeGI' is on, but that the object receives GI from Light Probes instead. Additional resources: ReceiveGI.LightProbes.All colors can be adjusted under Preferences > Colors.  
* * *
