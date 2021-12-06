<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
  <html>
  <body>
    <table border="1">
      <tr>
        <th>Name</th>
        <th>Age</th>
      </tr>
      <xsl:for-each select="CLASS/STUDENT[GRADE='A']">
      <tr>
        <td><xsl:value-of select="NAME"/></td>
        <td><xsl:value-of select="AGE"/></td>
      </tr>
      </xsl:for-each>
    </table>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>