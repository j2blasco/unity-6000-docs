* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-structuring-ui-templates.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html)
  * Use UXML instances as templates


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-structuring-ui-elements.html)
Work with elements
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-styling-ui-using-uss-selectors.html)
Style UI with UI Builder
# Use UXML instances as templates
You can instantiate existing UXML Documents as **Templates** inside your UXML Documents as **Template Instances** , similar to how [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) work in Unity. 
## Use a UXML Document as a template
To use an existing UXML Document in your project as a template, do the following:
  1. Under the **Library** ’s **Project** tab, find the UXML Asset (`.uxml`) you wish to instantiate.
  2. Drag it into the **Hierarchy** like an element in the **Library**.


A **Template Instance** appears in the **Hierarchy** like a normal element of type `TemplateContainer`. The name of the `.uxml` file displays as greyed font to the right of its name. If you expand the **Template Instance** , you can see the internal hierarchy of the instance. This internal hierarchy, as explained in [Working with elements](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-structuring-ui-elements.html), is read-only and only for reference. 
## Make a Sub-Document as a template
You can make a Sub-Document within a UXML Document as a **Template Instance** , so you can reuse it.
  1. Right-click on the Sub-Document.
  2. Select **Create Template**.
  3. Select a location to save the file.


This also instantiates the Sub-Document as **Template Instances** in the existing document.
**Note:** The properties of the parent or child elements of Sub-Document do not apply to the template container element.
## Edit a UXML document template instance
To edit an original UXML Document used as a **Template Instance** , right-click on a **Template Instance** , and select one of the following options:
  * **Open in UI Builder** : Unload the current UXML Document, and load the **Template Instance** :
![Open in UI Builder example](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIBuilder/OpenSubDocumentNormally.png) Open in UI Builder example
  * **Open Instance in Isolation** : Keep the current UXML Document loaded in the background while loading **Template Instance**. The **Hierarchy** and the **Canvas** only display the contents of the **Template Instance** , and the **StyleSheets** pane includes the style sheet of the background parent UXML Document in a read-only state. This is because the style sheets are still being applied to the **Template Instance** :
![Open Instance in Isolation example](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIBuilder/EditAsSubDocumentInIsolation.png) Open Instance in Isolation example
  * **Open Instance in Context** : Keep the current UXML Document loaded while making all its elements read-only and appear dimmed in the **Hierarchy** and the **Canvas**. You can edit the contents of the **Template Instance** within the context of the parent UXML Document. Use this option to update **Template Instance** content without losing the context of the host document:
![Open Instance in Context example](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIBuilder/EditAsSubDocumentInPlace.png) Open Instance in Context example
  * **Show in Project** : Show the location of the **Template Instance** file in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow).


For the second and third options, a breadcrumb appears above the ****Viewport** The user’s visible area of an app on their screen.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Viewport)**. You can use the breadcrumb to go back to a parent UXML Document.
![Sub-document breadcrumbs example](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIBuilder/SubDocumentBreadcrumbs.png) Sub-document breadcrumbs example
## Unpack a UXML document template instance
To unpack a single **Template Instance** , right-click on a **Template Instance** and select **Unpack Instance**. This changes **Template Instance** to a normal UXML Document.
To unpack all the **Template Instances** , right-click on a **Template Instance** and select **Unpack Instance Completely**. This changes all the **Template Instances** to normal UXML Documents.
## Additional resources
  * [Reuse UXML files](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-reuse-uxml-files.html)
  * [Encapsulate UXML documents with logic](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-encapsulate-uxml-with-logic.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-structuring-ui-elements.html)
Work with elements
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-styling-ui-using-uss-selectors.html)
Style UI with UI Builder
