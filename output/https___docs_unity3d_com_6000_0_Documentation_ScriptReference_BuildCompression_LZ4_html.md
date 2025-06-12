* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.LZ4.html

#  [BuildCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.html).LZ4
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
[BuildCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.html) LZ4; 
### Description
LZ4HC "Chunk Based" Compression.
LZ4HC (LZ4 High Compression) compression results in smaller compressed file sizes than LZ4 and larger compressed file sizes than LZMA, but does not require the entire bundle to be decompressed before use like LZMA. LZ4(HC) is a “chunk-based” algorithm, and therefore when objects are loaded from an LZ4(HC)-compressed bundle, only the corresponding chunks for that object are decompressed. This occurs on-the-fly, meaning there are no wait times for the entire bundle to be decompressed before use. The LZ4 Format was introduced in Unity 5.3 and was unavailable in prior versions.  
  
This BuildCompression is only supported for building Asset Bundles and is not available for recompression at runtime. Use LZ4Runtime for runtime recompression.
* * *
