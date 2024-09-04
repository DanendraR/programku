<?php
$warnet = array("Paket 1 jam", "Paket 2 jam", "Paket 3 jam"); # data paket yang tersedia
$pilih_paket = "Paket 3 jam"; # paket yang dipilih
$paket_tersedia = false; #  untuk mengecek apakah paket sudah ditemukan

foreach ($warnet as $pilihan) {
    if ($pilihan === $pilih_paket) {
        $paket_tersedia = true;
        break; # keluar dari perulangan jika paket sudah ditemukan
    }
}

if ($paket_tersedia) {
    echo "paket " . $pilih_paket . " Bisa di gunakan";
} else {
    echo "paket " . $pilih_paket . " tidak ready gan";
}
?>