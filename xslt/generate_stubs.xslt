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
            <xsl:variable name="stubName" select="replace(@name,'Service','Stubs')"/>
<xsl:result-document href="target/generated/test/java/{string-join(tokenize(@package,'\.'),'/')}/{$stubName}.java">
package <xsl:value-of select="@package"/>

class <xsl:value-of select="$stubName"/> {

    public void behaviour() {
<xsl:if test="result/artifact">
        doReturn(<xsl:value-of select="result/artifact/concat(@class, '.', @name)"/>).when(<xsl:value-of select="@name"/>).call(<xsl:value-of select="string-join(param/artifact/concat(@class,'.',@name),', ')"/>)
</xsl:if>
    }
}
</xsl:result-document>
        </xsl:for-each>
	</xsl:template>

</xsl:stylesheet>

