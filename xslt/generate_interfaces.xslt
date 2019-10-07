<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE xml>
<xsl:stylesheet version="2.0"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:zenta="http://magwas.rulez.org/zenta"
	xmlns:zentatools="java:org.rulez.magwas.zentatools.XPathFunctions"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:output method="xml" version="1.0" encoding="utf-8"
		indent="yes" omit-xml-declaration="yes" />

	<xsl:include href="xslt/functions.xslt" />

	<xsl:param name="outputbase" />
    <xsl:variable name="doc" select="/"/>

    <xsl:variable name="services" select="zenta:gatherServices(/)"/>

	<xsl:template match="/" mode="java">
        <xsl:for-each select="$services">
        <xsl:variable name="params">
            <xsl:for-each select="param">
                <param>
                <xsl:attribute name="p" select="concat(@type, ' ', @name)"/>
                </param>
            </xsl:for-each>
        </xsl:variable>
<xsl:result-document href="target/generated/main/java/{string-join(tokenize(@package,'\.'),'/')}/{@name}.java">
package <xsl:value-of select="@package"/>

class <xsl:value-of select="@name"/> {

    <xsl:value-of select="@type"/> call (<xsl:value-of select="string-join($params//@p, ', ')"/>)
}
</xsl:result-document>
        </xsl:for-each>
	</xsl:template>

</xsl:stylesheet>

