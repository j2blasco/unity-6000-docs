* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-fontNames.html

#  [TrueTypeFontImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter.html).fontNames
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
fontNames; 
### Description
An array of font names, to be used when includeFontData is set to false.
If you a trying to render a glyph which is not available in this font, Unity will walk through the list of font names given to find another font which has that glyph. For each name on the list, it will first search the supplied fontReferences for matching fonts in your project and then it will search fonts installed in the OS for matching fonts.  
  
Additional resources: [TrueTypeFontImporter.fontReferences](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-fontReferences.html).
* * *
