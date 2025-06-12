* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-styling-ui-using-uss-variables.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html)
  * Assign USS variables in UI Builder


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-styling-ui-using-uss-selectors.html)
Style UI with UI Builder
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-testing-ui.html)
Test UI
# Assign USS variables in UI Builder
[USS variables](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-variables.html) define values that you can reuse in other USS rules. USS variables are primarily used for themes, with the default Unity themes exposing a long list of standard variables to make your UI more consistent with standard controls.
You can’t create USS variables with UI Builder. You must use a text editor to create a new USS variable in the USS file.
You can assign a USS variable that’s in the current theme or any assigned StyleSheets to the current UI Document (UXML) to a style property in UI Builder. When you work on an Editor UI, make sure to [enable **Editor Extension Authoring**](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-interface-overview.html#enable-editor-extension-authoring-for-ui-documents-uxml) to see all available Editor variables.
To assign a variable:
  1. In the StyleSheet window, select the selector.
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, right-click a style field.
  3. Select **Set Variable**. This converts the style field into a text field.
  4. Enter the name of the USS variable. As you type the name of the variable, a dropdown list displays the available variables.
![USSVariablesSearch](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIBuilder/USSVariablesSearch.png) USSVariablesSearch
You can also select a variable from the dropdown list, and see its current value and the StyleSheet asset it’s coming from. Pressing **Enter** sets the variable and reverts the style field back to its original type.
**Tip** : For style fields that are already text fields, you can also assign a variable by starting to type `--` instead of a number.


You can identify which style fields have a variable assigned by checking if the field’s label has a chain icon on the left.
![USSVariablesSet](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIBuilder/USSVariablesSet.png) USSVariablesSet
To remove a variable assignment, right-click a style field and select **Remove Variable**.
**Note** : Any inline styles set on a style property will override the USS variables.
## Additional resources
  * [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-styling-ui-using-uss-selectors.html)
Style UI with UI Builder
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-testing-ui.html)
Test UI
