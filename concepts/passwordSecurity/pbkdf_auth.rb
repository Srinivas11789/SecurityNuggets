# Reference: https://ruby-doc.org/stdlib-2.0.0/libdoc/openssl/rdoc/OpenSSL/PKCS5.html
require "openssl"


pass = "secret"
salt = OpenSSL::Random.random_bytes(16)
iter = 200000
hash = OpenSSL::Digest::SHA256.new
len = hash.digest_length


def hash(pass, salt, iter, len, hash)
  value = OpenSSL::PKCS5.pbkdf2_hmac(pass, salt, iter, len, hash)
  return value
end

def eql_time_cmp(a, b)
  unless a.length == b.length
    return false
  end
  cmp = b.bytes
  result = 0
  a.bytes.each_with_index {|c,i|
    result |= c ^ cmp[i]
  }
  result == 0
end

def main()
    puts "Set you password: "
    pass = gets
    salt = OpenSSL::Random.random_bytes(16)
    iter = 200000
    hash = OpenSSL::Digest::SHA256.new
    len = hash.digest_length
    pass_hash = hash(pass, salt, iter, len, hash)
    while 1
    	puts "Try to make password guess: "
    	guess = gets
    	guess_hash = hash(guess, salt, iter, len, hash)
    	if eql_time_cmp(pass_hash, guess_hash)
       		puts "Accepted!"
    	else
       		puts "Failed! Try Again."
    	end
    end
end

main()



