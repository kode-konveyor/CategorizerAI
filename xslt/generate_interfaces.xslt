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

    <xsl:function name="zenta:fullPackageName">
        <xsl:param name="doc"/>
        <xsl:param name="package"/>
        <xsl:for-each select="$package">
        <xsl:variable name="parent" select="zenta:neighbours($doc,.,'contains,2')"/>
        <xsl:value-of select="
            if(@xsi:type = 'Package')
            then
                if($parent/@xsi:type = 'Package')
                then
                    concat(string-join(zenta:fullPackageName($doc,$parent),''),'.',@name)
                else
                    @name
            else
                ''
        "/>
        </xsl:for-each>
    </xsl:function>
    <xsl:variable name="services">
		<xsl:for-each select="//element[@xsi:type='Service']">
            <service>
                <xsl:copy-of select="@name"/>
                <xsl:attribute name="type" select="zenta:neighbours(/,.,'results,1;is of/is type of,1')/@name"/>
                <xsl:attribute name="package" select="zenta:fullPackageName(/,zenta:neighbours(/,.,'is implemented by/implements,2;contains,2'))"/>
                <xsl:for-each select="zenta:neighbours(/,.,'uses,1')">
                    <xsl:sort select="value[@ancestorName='referenced as/references']/@name"/>
                    <param>
                        <xsl:variable name="businessObject" select="zenta:neighbours($doc,.,'is/is used as parameter,1')"/>
                        <xsl:copy-of select="$businessObject/value[@ancestorName='is/is used as parameter']/@name"/>
                        <xsl:attribute name="type" select="$businessObject/value[@ancestorName='is of/is type of']/@name"/>
                    </param>
                </xsl:for-each>
            </service>
		</xsl:for-each>
    </xsl:variable>

	<xsl:template match="/">
        <xsl:for-each select="$services/*">
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

