* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-useLegacyProbeSampleCount.html

#  [EditorSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings.html).useLegacyProbeSampleCount
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
useLegacyProbeSampleCount; 
### Description
Enable the legacy fixed sample counts for baking Light Probes with Progressive Lightmapper.
The fixed sample counts are: 64 direct samples, 2048 indirect samples and 2048 environment samples. Disabling this ties the Light Probe sample counts to the sample counts specified for lightmaps. When disabled a multiplier is provided in the lighting settings to be able to use more samples for Light Probes. This is because a Light Probe covers a larger area than a lightmap texel so generally needs more samples to converge.
* * *
