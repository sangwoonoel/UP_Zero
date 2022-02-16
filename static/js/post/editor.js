CKEDITOR.on("dialogDefinition", function (e) {
  let dialogName = e.data.name;
  let dialogDefinition = e.data.definition;

  if (dialogName === "image") {
    let infoTab = dialogDefinition.getContents("info");
    if (infoTab) {
      infoTab.remove("txtAlt");
      infoTab.remove("txtHSpace");
      infoTab.remove("txtVSpace");
      infoTab.remove("cmbAlign");
      infoTab.remove("txtBorder");
    }
  }
});

CKEDITOR.config.removeDialogTabs =
  "image:Link;image:advanced;link:target;link:advanced";
CKEDITOR.config.image_previewText = CKEDITOR.tools.repeat("미리보기 텍스트", 1);
