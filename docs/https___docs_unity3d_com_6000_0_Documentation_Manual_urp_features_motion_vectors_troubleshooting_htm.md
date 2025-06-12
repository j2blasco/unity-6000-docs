* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-troubleshooting.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Motion vectors in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-landing.html)
  * Troubleshooting motion vectors in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-sample.html)
Sample motion vectors in a shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-reference.html)
Motion vectors settings reference for URP
# Troubleshooting motion vectors in URP
Solve common issues with motion vectors in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP).
## Fix motion vectors that are too large
If a **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) is locked to an object that moves, for example, a model of a car in a racing game, select the **Per Object Motion** option in the **Motion Vectors** property of that object. If you don’t select that option, the object will have incorrectly large motion vectors. This happens because Unity calculates camera motion vectors assuming that the geometry of the object is static in the world, and that the camera is moving relative to it. This might cause significant TAA or motion blur artifacts.
## Fix visual artefacts
When the motion vector texture is used by full-screen **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effects, such as TAA and motion blur, any screen regions with incorrect motion vectors (either missing, or inaccurate) will likely exhibit visual artifacts. The artifacts can include: texture blurring, movement ghosting, improper anti-aliasing, non-realistic or inappropriate motion blur, and so on.
If you are experiencing artifacts that you suspect are caused by incorrect motion vectors, check if the affected objects have object motion vector rendering enabled. In the **Frame Debugger** , the object should be present in the **MotionVectors** pass. To troubleshoot missing or incorrect motion vectors for a particular object, refer to the section [Cases when Unity renders motion vectors](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors.html#cases-when-motion-vectors).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-sample.html)
Sample motion vectors in a shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-reference.html)
Motion vectors settings reference for URP
