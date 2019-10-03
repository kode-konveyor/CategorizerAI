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
	<xsl:param name="baseuri" />

	<xsl:variable name="testcases">
		<testcases>
			<xsl:call-template name="testcases" />
		</testcases>
	</xsl:variable>

	<xsl:template match="/">
		<xsl:result-document
			href="{$outputbase}testcases.txt">
			<xsl:copy-of
				select="zenta:writeTestcasesAsText($testcases)" />
		</xsl:result-document>
		<xsl:result-document
			href="{$outputbase}testcases.xml">
			<xsl:copy-of select="$testcases" />
		</xsl:result-document>
	</xsl:template>

	<xsl:function name="zenta:writeTestcasesAsText">
		<xsl:param name="testcases" />
		<xsl:for-each select="$testcases//testcase">
----------------------------------------------------------------------------
## <xsl:value-of select="@type"/>: <xsl:value-of select="@name" />
    @TestedFeature("<xsl:value-of select="@feature" />")
    @TestedOperation("<xsl:value-of select="@operation" />")
    @TestedBehaviour("<xsl:value-of select="@testcase" />")
<xsl:text> </xsl:text>

<xsl:value-of select="replace(doc,'^[ \t\n]+','')" />

You should modify *<xsl:value-of select=".//service/@name"/>*

relevant images:

<xsl:for-each select=".//img">
[![<xsl:value-of select="@name"/>](<xsl:value-of select="concat($baseuri,'/pics/',@id,'.png')"/>)](<xsl:value-of select="concat($baseuri,'/index.html#',@id)"/>)
<xsl:value-of select="@name"/>
</xsl:for-each>
<xsl:text>
</xsl:text>
		</xsl:for-each>
	</xsl:function>

	<xsl:template name="testcases">
		<xsl:variable name="root" select="/" />
		<xsl:for-each
			select="//element[@xsi:type='Policy']">
			<xsl:variable name="feature" select="." />
			<xsl:for-each
				select="zenta:neighbours(/,$feature,'drives,1')">
				<xsl:variable name="operation" select="." />
				<xsl:for-each
					select="zenta:neighbours($root,$operation,'determines,1')">
					<xsl:variable name="testcase" select="." />
					<testcase
						name="{concat($feature/@name,'/', $operation/@name, '; ', $testcase/@name)}"
						feature="{$feature/@name}" operation="{$operation/@name}"
						testcase="{$testcase/@name}" featureid="{$feature/@id}"
						operationid="{$operation/@id}" testcaseid="{$testcase/@id}"
                        type="{$testcase/@xsi:type}">
                        <doc><xsl:copy-of select="$testcase/documentation/(text()|*)" /></doc>
                            <xsl:for-each select="zenta:neighbours($root,$testcase,'is implemented by/implements,1')">
                                <xsl:variable name="service" select="."/>
                                <xsl:variable name="step" select="zenta:neighbours($root,$service,'is implemented by/implements,2')"/>
                        <service>
                                <xsl:copy-of select="@name"/>
                            <xsl:for-each select="//element[@xsi:type='zenta:ZentaDiagramModel' and (.//child[@zentaElement=$service/@id] or .//child[@zentaElement=$testcase/@id] or .//child[@zentaElement=$step/@id])]">
                                <img>
                                    <xsl:copy-of select="@name|@id"/>
                                </img>
                            </xsl:for-each>
                        </service>
                            </xsl:for-each>
					</testcase>
				</xsl:for-each>
			</xsl:for-each>
		</xsl:for-each>
	</xsl:template>

</xsl:stylesheet>

