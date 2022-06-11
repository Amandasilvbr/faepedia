<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="shortcut icon" href="logo.svg">
        <link rel="stylesheet" href="css/style.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Cousine">
        <link rel="stylesheet" id="platformStylesheet">
        <title>Faepedia - Equipment</title>
    </head>
    <body>
        <script src="js/format.js" onload="platformFormat('css')"></script>
        <p><a href="./">Back to homepage</a></p>
        <table>
            <thead>
                <tr>
                    <th>Type</th>
                    <th>Name</th>
                    <th>Cost</th>
                    <th>Weight</th>
                    <th>Tags</th>
                </tr>
            </thead>
            <tbody>
<?php foreach ($equipment as $item): ?>
                <tr id="<?= $item["name"]; ?>">
                    <td><?= $item["type"]; ?></td>
                    <td><b><?= $item["name"]; ?></b></td>
                    <td><?= pluralize($item["cost"], "gold piece", "cost"); ?></td>
                    <td><?= pluralize($item["weight"], "pound", "weight"); ?></td>
                    <td><?= strlen($item["tags"]) > 0 ? $item["tags"] : "No applicable tags"; ?></td>
                </tr>
<?php endforeach; ?>
            </tbody>
        </table>
    </body>
</html>
