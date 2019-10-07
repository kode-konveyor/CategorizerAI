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

    <xsl:variable name="testData">
		<xsl:for-each select="//element[@xsi:type='TestData']">
            <testData>
                <xsl:copy-of select="@name"/>
                <xsl:attribute name="package" select="zenta:fullPackageName(/,zenta:neighbours(/,.,'contains,2'))"/>
                <xsl:for-each select="zenta:neighbours($doc,.,'contains,1')[@xsi:type='Test Artifact']">
                    <artifact>
                    <xsl:copy-of select="@name"/>
                    <xsl:attribute name="type" select="value[@ancestorName='is a/is type of']/@name"/>
                    <xsl:copy-of select="documentation/text()"/>
                    </artifact>
                </xsl:for-each>
            </testData>
		</xsl:for-each>
    </xsl:variable>

	<xsl:template match="/" mode="java">
        <xsl:for-each select="$testData//testData">
<xsl:result-document href="target/generated/test/java/{string-join(tokenize(@package,'\.'),'/')}/{@name}.java">
package <xsl:value-of select="@package"/>

class <xsl:value-of select="@name"/> {

<xsl:for-each select="artifact">
<xsl:text>  </xsl:text><xsl:value-of select="@type"/><xsl:text> </xsl:text><xsl:value-of select="@name"/><xsl:text> </xsl:text>=<xsl:text> </xsl:text><xsl:value-of select="text()"/>;
</xsl:for-each>

}
</xsl:result-document>
        </xsl:for-each>
	</xsl:template>

</xsl:stylesheet>

