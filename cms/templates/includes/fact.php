<?php
$cache_file = 'cache.txt';
$facts_file = 'facts.txt';
$old_facts_file = 'oldfacts.txt';

function read_and_delete_first_line($filename) {
    $file = file($filename);
    $output = $file[0];
    unset($file[0]);
    file_put_contents($filename, $file);
    return $output;
}

if (file_exists($cache_file) && filemtime($cache_file) > time() - 604600) {
    echo file_get_contents($cache_file);
}

else {
    $content = read_and_delete_first_line($facts_file);
    $today_content = file_get_contents($cache_file);
    file_put_contents($old_facts_file, "\n" . "<br>" . $today_content, FILE_APPEND);
    file_put_contents($cache_file, $content);
    echo $content;
} ?>


