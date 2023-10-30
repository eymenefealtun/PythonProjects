from rembg import remove

input_path = "temp.jpg";
output_path = "output.png"; # arkasi transparan olan resimler png oluyor

with open(input_path, 'rb') as i: ## rb'deki b binary den geliyor. 01 leri okuyaracak acicagi anlamina geliyor dosyayi (read binary)
    with open(output_path,'wb') as o: ## write binary
        input_file = i.read()
        output_file = remove(input_file)
        o.write(output_file)