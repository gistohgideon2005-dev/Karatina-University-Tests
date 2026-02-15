import java.security.SecureRandom

/**
 * Simple, secure password generator utility for this repo.
 * Usage (from command line):
 *   groovy Scripts/library/Utils/passwordGenerator.groovy 20 true true true true
 * Arguments: length includeUpper includeLower includeDigits includeSymbols
 */

class PasswordGenerator {
    static final String UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    static final String LOWER = 'abcdefghijklmnopqrstuvwxyz'
    static final String DIGITS = '0123456789'
    static final String SYMBOLS = '!@#$%^&*()-_=+[]{};:,.<>?'

    static final SecureRandom random = new SecureRandom()

    static String generate(int length = 16, boolean useUpper = true, boolean useLower = true, boolean useDigits = true, boolean useSymbols = true) {
        def pools = []
        if (useUpper) pools << UPPER
        if (useLower) pools << LOWER
        if (useDigits) pools << DIGITS
        if (useSymbols) pools << SYMBOLS
        if (pools.isEmpty()) throw new IllegalArgumentException('At least one character class must be enabled')

        // Ensure at least one character from each selected pool
        def chars = []
        pools.each { pool -> chars << pool.charAt(random.nextInt(pool.length())) }

        while (chars.size() < length) {
            def pool = pools[random.nextInt(pools.size())]
            chars << pool.charAt(random.nextInt(pool.length()))
        }

        Collections.shuffle(chars, random)
        return chars.join()
    }

    static void main(String[] args) {
        int length = (args.length > 0) ? args[0].toInteger() : 16
        boolean u = (args.length > 1) ? args[1].toBoolean() : true
        boolean l = (args.length > 2) ? args[2].toBoolean() : true
        boolean d = (args.length > 3) ? args[3].toBoolean() : true
        boolean s = (args.length > 4) ? args[4].toBoolean() : true

        try {
            println generate(length, u, l, d, s)
        } catch (IllegalArgumentException e) {
            System.err.println('Error: ' + e.message)
            System.exit(2)
        }
    }
}
