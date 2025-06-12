* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-fontReferences.html

#  [TrueTypeFontImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter.html).fontReferences
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
fontReferences; 
### Description
References to other fonts to be used looking for fallbacks.
This is a list of references to other Font assets in your project, which will be used when looking for the fallback fonts listed in fontNames when trying to render a character which is not available in the font. If you set the fallback font names in the Font importer inspector in the editor, Unity will automatically search your project for matching assets and populate the references automatically - so you should only ever need to set this yourself when importing Font assets programmatically.  
  
Additional resources: [TrueTypeFontImporter.fontNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter-fontNames.html).
* * *
