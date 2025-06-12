* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-troubleshoot.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Profile rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/profile-rendering.html)
  * [Frame Timing Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-landing.html)
  * Troubleshooting the Frame Time Manager


[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-record-timing-data.html)
Record frame timing data
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerRendering.html)
Rendering Profiler module reference
# Troubleshooting the Frame Time Manager
For GPUs that use tile-based deferred rendering architecture, such as Metal GPUs in Apple devices, the reported GPU Time might be larger than the reported frame time.
This can happen when the GPU is under heavy load, or when the GPU pipeline is full. In these cases, the GPU might defer execution of some rendering phases. Because the FrameTimingManager measures the time between the beginning and end of the frame rendering, any gaps between phases increase the reported GPU time.
In the example below, no GPU resources are available, because the GPU passes a job from the Vertex queue to the Fragment queue. The GPU’s graphics API therefore defers the execution of the next phase. When this happens, the GPU time measurement includes phase work time and any gap in between. The result is that the FrameTimingManager reports a higher GPU time measurement than expected.
![Diagram showing how the discrepancy in reported GPU time can happen in the Metal API](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/frame-timing-manager-deferred-rendering-diagram.png) Diagram showing how the discrepancy in reported GPU time can happen in the Metal API
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-record-timing-data.html)
Record frame timing data
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerRendering.html)
Rendering Profiler module reference
